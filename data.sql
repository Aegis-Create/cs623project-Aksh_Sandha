INSERT INTO Product (prodid, pname, price) VALUES
('p1', 'pen', 1.50),
('p2', 'pencil', 0.50),
('p3', 'notebook', 3.00);

INSERT INTO Depot (depid, addr, volume) VALUES
('d1', 'New York', 100),
('d2', 'Boston', 200),
('d3', 'Chicago', 300);

INSERT INTO Stock (prodid, depid, quantity) VALUES
('p1', 'd1', 20),
('p1', 'd2', 30),
('p2', 'd1', 40),
('p2', 'd3', 10),
('p3', 'd2', 15);
