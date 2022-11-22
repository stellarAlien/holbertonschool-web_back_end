export default  function getListStudentIds(...students) {
    const ids = students.map((student) => student.id);
    return ids;
}