export default function createReportObject(employeesList) {
    return {
        allemployees: {...employeesList},
        getNumberOfDepartments (employeesList) {
            return Object.keys(employeesList).length;
        },
    };
    }