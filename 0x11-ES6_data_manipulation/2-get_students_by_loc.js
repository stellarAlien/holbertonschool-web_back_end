export default function getStudentsByLocation(city, ...students) {
    const city_students = students.filter(student => student.city == city);
    return city_students;
}

