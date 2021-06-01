module.exports = function createPushNotificationsJobs(jobs) {
    if (!Array.isArray(jobs)){
        throw Error('Jobs is not an array')
    }
    jobs.forEach((val) => {
        const job = queue.create('push_notification_code_3', val)
        .save((error) => {
            if (!error) console.log(`Notification job created: ${job.id}`);
        })
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });
    
        job.on('failed', (errorMessage) => {
            console.log(`Notification job ${job.id} failed: ${errorMessage}`);
        });
    
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    })
    

}



