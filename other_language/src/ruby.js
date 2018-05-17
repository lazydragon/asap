const exec = require('child_process').exec;

exports.handler = function(event, context) {
    const child = exec('./lambdaRuby.rb ', (result) => {
        // Resolve with result of process
        context.done(result);
    });

    // Log process stdout and stderr
    child.stdout.on('data', console.log);
    child.stderr.on('data', console.error);
}
