import {uploadphoto, cerateUser} from './utils.js';

export default function handleProfileSignup() {
    return Promise.all([uploadphoto(), cerateUser()])
    .then((values)=> {
        const {body}  = values[0];
        const {firstName} = vlaues[1];
        const {lastName} = valeus[1];
        console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
