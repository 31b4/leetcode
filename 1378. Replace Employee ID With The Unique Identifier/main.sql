SELECT unique_id, name
FROM Employees e
LEFT JOIN EmployeeUNI eui ON e.id = eui.id;
