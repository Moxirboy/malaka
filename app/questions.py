def questions():
        import sqlite3

        # Connect to the SQLite database
        conn = sqlite3.connect('shoshilinch.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Write a query to select a random row
        query = "SELECT id,question FROM test ORDER BY RANDOM() LIMIT 1;"

        # Execute the query
        cursor.execute(query)

        # Fetch the result
        random_row = cursor.fetchone()
        return_choices=[]
        if random_row:
            # Assuming the question_id is the second column in your random row
            question_id = random_row[0]

            # Write a query to select text from the choice table where question_id matches
            query2 = "SELECT text FROM choice WHERE question_id=?"
            
            # Create another cursor object
            cursor2 = conn.cursor()
            
            # Execute the query with the question_id as the parameter
            cursor2.execute(query2, (question_id,))
            
            # Fetch all the choices
            choices = cursor2.fetchall()
            
            # Print the choices
            
            for choice in choices:
                return_choices.append(choice[0])
            
            # Close the second cursor
            cursor2.close()

        # Close the connection
        conn.close()
        return random_row,return_choices