export default  function signUpUser(firstName, lastName) {
    return Promise((resolve, reject) => {
        resolve({
            firstName: firstName,
            lastName: lastName,
          })
    })
}