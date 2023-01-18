<!DOCTYPE html>
<html>

<head>
    <title>Table with database</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            color: #1e90ff;
            font-family: Consolas, Monospace;
            font-size: 25px;
            text-align: center;
        }

        th {
            background-color: rgb(118, 205, 216);
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2
        }
    </style>
</head>

<body>
    <table>
        <tr>
            <th>PersonID</th>
            <th>FirstName</th>
            <th>LastName</th>
            <th>Age</th>
        </tr>
        <?php
        $conn = mysqli_connect("mysql_docker", "root", "1234", "people");
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        $sql = "SELECT PersonID, FirstName, LastName, Age FROM customers  WHERE Age = 22 ";

        $result = $conn->query($sql);
        if ($result->num_rows > 0) {
            // output data of each row
            while ($row = $result->fetch_assoc()) {
                echo "<tr><td>" . $row["PersonID"] . "</td><td>" . $row["FirstName"] . "</td><td>"
                    . $row["LastName"] . "</td><td>" . $row["Age"] . "</td></tr>";
            }
            echo "</table>";
        } else {
            echo "0 results";
        }
        $conn->close();
        ?>
    </table>
</body>

</html>