export default function getListStudents() {
    let students = [
    {firstName: 'Guillaume', id: 1, location: 'San Francisco'},
    {firstName: 'James', id: 2, location: 'Columbia'},
    {fistName: 'Serena', id: 5, location: 'San Francisco'},
    ];

    let arrayObject = Object.values(students); 
    return arrayObject;
}