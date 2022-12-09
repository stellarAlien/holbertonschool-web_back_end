const kue = require("kue");

const blacklist = [4153518780, 4153518781];
let push_notification_code_2 = kue.createQueue()
async function sendNotification( phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blacklist.includes(phoneNumber)) {
        done( new Error(`Phone number ${phoneNumber} is blacklisted`));}
    } else {
        job.progress(50, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        done();
    };
    push_notification_code_2.process('message', 2, (job, done) => {
        const {phoneNumber, message} = job.data;
        sendNotification(phoneNumber, message, job, done) ;
    ;});