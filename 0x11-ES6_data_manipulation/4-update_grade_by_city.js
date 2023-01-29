export default function getStudentsByLocation(array, city, grad) {
  return array
    .filter((i) => i.location === city)
    .map((student) => {
      const student_grade = grad
        .filter((i) => i.studentId === student.id)
        .map((x) => x.grade)[0];
      const grade = student_grade || 'N/A';
      return { ...student, grade };
    });
}
