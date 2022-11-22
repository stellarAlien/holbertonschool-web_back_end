export default function updateStudentGradeByCity(students, city, newGrades) {
    if(Array.isArray(students)) {
    const filtered = students.filter(i => i.city == city)
    filtered.map(s => {
        data = newGrades.filter((grade => grade.studentId == s.id));
        return {s, grade: data ? data.grade :'N/A'};
    });
}
    throw new Error('getListStudent is not an Array');
} 