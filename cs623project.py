import psycopg2


# Connection helper

def get_connection():
    return psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Aksh123!',
        database='cs623project'
    )


# 1) Delete product p1 (Product + Stock via CASCADE)

def transaction_delete_product(p_id='p1'):
    conn = get_connection()
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM Product WHERE prodid = %s", (p_id,))

        conn.commit()
        print("Transaction 1: Deleted product", p_id, "and related stock (via ON DELETE CASCADE).")

    except Exception as e:
        conn.rollback()
        print("Transaction 1 rolled back due to error:", e)

    finally:
        cursor.close()
        conn.close()



# 2) Delete depot d1 (Depot + Stock via CASCADE)


def transaction_delete_depot(d_id='d1'):
    conn = get_connection()
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM Depot WHERE depid = %s", (d_id,))

        conn.commit()
        print("Transaction 2: Deleted depot", d_id, "and related stock (via ON DELETE CASCADE).")

    except Exception as e:
        conn.rollback()
        print("Transaction 2 rolled back due to error:", e)

    finally:
        cursor.close()
        conn.close()


# 3) Rename product p1 -> pp1 in Product and Stock


def transaction_rename_product(old_id='p1', new_id='pp1'):
    conn = get_connection()
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE Product SET pname = %s WHERE prodid = %s",
            ('pp1_name', old_id)
        )

        cursor.execute(
            "UPDATE Product SET prodid = %s WHERE prodid = %s",
            (new_id, old_id)
        )

        conn.commit()
        print(f"Transaction 3: Renamed product {old_id} to {new_id} in Product and Stock (ON UPDATE CASCADE).")

    except Exception as e:
        conn.rollback()
        print("Transaction 3 rolled back due to error:", e)

    finally:
        cursor.close()
        conn.close()



# 4) Rename depot d1 -> dd1 in Depot and Stock


def transaction_rename_depot(old_id='d1', new_id='dd1'):
    conn = get_connection()
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE Depot SET addr = %s WHERE depid = %s",
            ('New address for ' + new_id, old_id)
        )

        cursor.execute(
            "UPDATE Depot SET depid = %s WHERE depid = %s",
            (new_id, old_id)
        )

        conn.commit()
        print(f"Transaction 4: Renamed depot {old_id} to {new_id} in Depot and Stock (ON UPDATE CASCADE).")

    except Exception as e:
        conn.rollback()
        print("Transaction 4 rolled back due to error:", e)

    finally:
        cursor.close()
        conn.close()



# 5) Add product (p100, cd, 5) and stock (p100, d2, 50)


def transaction_add_product_with_stock():
    conn = get_connection()
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO Product (prodid, pname, price) VALUES (%s, %s, %s)",
            ('p100', 'cd', 5)
        )

        cursor.execute(
            "INSERT INTO Stock (prodid, depid, quantity) VALUES (%s, %s, %s)",
            ('p100', 'd2', 50)
        )

        conn.commit()
        print("Transaction 5: Inserted product p100 and stock (p100, d2, 50).")

    except Exception as e:
        conn.rollback()
        print("Transaction 5 rolled back due to error:", e)

    finally:
        cursor.close()
        conn.close()



# 6) Add depot (d100, Chicago, 100) and stock (p1, d100, 100)


def transaction_add_depot_with_stock():
    conn = get_connection()
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO Depot (depid, addr, volume) VALUES (%s, %s, %s)",
            ('d100', 'Chicago', 100)
        )

        cursor.execute(
            "INSERT INTO Stock (prodid, depid, quantity) VALUES (%s, %s, %s)",
            ('p1', 'd100', 100)
        )

        conn.commit()
        print("Transaction 6: Inserted depot d100 and stock (p1, d100, 100).")

    except Exception as e:
        conn.rollback()
        print("Transaction 6 rolled back due to error:", e)

    finally:
        cursor.close()
        conn.close()



# menu for demo


def main():
    print("CS623 Project – PostgreSQL / psycopg2 Transactions")
    print("1) Delete product p1")
    print("2) Delete depot d1")
    print("3) Rename product p1 -> pp1")
    print("4) Rename depot d1 -> dd1")
    print("5) Add product (p100, cd, 5) and stock (p100, d2, 50)")
    print("6) Add depot (d100, Chicago, 100) and stock (p1, d100, 100)")
    choice = input("Choose transaction (1–6): ").strip()

    if choice == '1':
        transaction_delete_product('p1')
    elif choice == '2':
        transaction_delete_depot('d1')
    elif choice == '3':
        transaction_rename_product('p1', 'pp1')
    elif choice == '4':
        transaction_rename_depot('d1', 'dd1')
    elif choice == '5':
        transaction_add_product_with_stock()
    elif choice == '6':
        transaction_add_depot_with_stock()
    else:
        print("Invalid choice.")


if __name__ == '__main__':
    main()
