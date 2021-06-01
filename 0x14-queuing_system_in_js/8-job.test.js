const chai = require('chai');

const createPushNotificationsJobs = require('./8-job.js')
const expect = chai.expect
const queue = require('kue').createQueue()

const jobs = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    },
    {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
    }
]

describe('createPushNotificationsJobs', () => {
	before(() => queue.testMode.enter())
	afterEach(() => queue.testMode.clear())
	after(() => queue.testMode.exit())

	it('displays an error message if jobs is not an array', () => {
		const obj = {
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account'
		}
		expect(() => createPushNotificationsJobs(obj, queue)).to.throw(Error, 'Jobs is not an array')
	})

	
})