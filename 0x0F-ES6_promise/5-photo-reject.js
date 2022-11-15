export default function uploadPhoto(filename) {
    return Promise((resolve, reject) => {
        reject(new Error(`{filename} cannot be processed`));
    });
}