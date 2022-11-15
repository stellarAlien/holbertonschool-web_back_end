import signUpUser from './4-user-promise.js'
import uploadPhoto from './5-uploadPhoto.js'

export default function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.allSettled([signUpUser(), uploadPhoto()]).then(() => {
        [
            {status: response.status}    
        ]   
    })
}