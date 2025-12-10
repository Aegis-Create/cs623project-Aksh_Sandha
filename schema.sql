CREATE TABLE Product (
    prodid CHAR(10),
    pname VARCHAR(30),
    price DECIMAL
);

ALTER TABLE Product ADD CONSTRAINT pk_product PRIMARY KEY (prodid);
ALTER TABLE Product ADD CONSTRAINT ck_product_price CHECK (price > 0);

CREATE TABLE Depot (
    depid CHAR(10),
    addr VARCHAR(50),
    volume INTEGER
);

ALTER TABLE Depot ADD CONSTRAINT pk_depot PRIMARY KEY (depid);
ALTER TABLE Depot ADD CONSTRAINT ck_depot_volume CHECK (volume > 0);

CREATE TABLE Stock (
    prodid CHAR(10),
    depid CHAR(10),
    quantity INTEGER
);

ALTER TABLE Stock ADD CONSTRAINT pk_stock PRIMARY KEY (prodid, depid);

ALTER TABLE Stock ADD CONSTRAINT fk_stock_prodid
    FOREIGN KEY (prodid)
    REFERENCES Product(prodid)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

ALTER TABLE Stock ADD CONSTRAINT fk_stock_depid
    FOREIGN KEY (depid)
    REFERENCES Depot(depid)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

ALTER TABLE Stock ADD CONSTRAINT ck_stock_quantity CHECK (quantity >= 0);
