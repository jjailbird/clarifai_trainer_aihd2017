var Botkit = require('botkit');
var request = require("request").defaults({ encoding: null });
var Clarifai = require('clarifai');

app_id = process.env.clarifai_app_id
app_secret = process.env.clarifai_app_secret
var ClarifaiApp = new Clarifai.App(
  app_id,
  app_secret
);

var controller = Botkit.slackbot({
  debug: false
  //include "log: false" to disable logging
  //or a "logLevel" integer from 0 to 7 to adjust logging verbosity
});

// connect the bot to a stream of messages
controller.spawn({
  token: process.env.slack_token,
}).startRTM()

// give the bot something to listen for.
controller.on('message_received', function(bot, message) {
    //console.log (message);
    if (message.type == "file_shared") {
      id = message.file_id;
      console.log("got file: "+ id);
      bot.api.files.info({file:id},function(err,response) {
        console.log("info: ", response);
        if (err) {
          return;
        }
        request.get({url:response.file.url_private_download,encoding:null,
                    headers:{"Authorization":"Bearer "+process.env.slack_token}}, function (err, res, body) {

          console.log("error:", err)
          console.log('statusCode:',  response.statusCode);
          console.log("*** calling clarify ...... ****")
          //console.log(body)
          ClarifaiApp.models.predict("smilies", body.toString('base64')).then(function(response){
            console.log("*** clarifai response ***")
            obj = JSON.stringify(response);
            console.log(obj)

            value = response.outputs[0].data.concepts[0].value;
            console.log("value:", value);

            if (parseFloat(value)>0.7) {
              emoji = "smile"
            } else if (parseFloat(value)>0.5) {
              emoji = "simple_smile"
            } else if (parseFloat(value)>0.3) {
              emoji = "expressionless"
            } else {
              emoji = "worried"
            }
            bot.api.reactions.add({file:id, name:emoji})


          }, function(err) {
            console.error("*** clarifai error ***")
            console.error(err);
          })
        });
      })
    }
    // carefully examine and
    // handle the message here!
    // Note: Platforms such as Slack send many kinds of messages, not all of which contain a text field!
});
