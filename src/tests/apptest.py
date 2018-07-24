import unittest
import mock
import app


class TestDuckCounter(unittest.TestCase):

    @mock.patch("app.DbConnector")
    def test_reads_counter_from_db(self, db_connector):
        app.db = db_connector
        db_connector.get_duck_count.return_value = 72;
        count = app.get_duck_count()
        self.assertEqual('Current duck count : 72 ducks.', count);

    @mock.patch("app.DbConnector")
    def test_decreases_counter_from_db(self, db_connector):
        app.db = db_connector
        db_connector.get_duck_count.return_value = 5;
        app.decrease_duck_count()
        db_connector.decrease_duck_count.assert_called_with();

    @mock.patch("app.DbConnector")
    def test_does_not_decrease_to_negative(self, db_connector):
        app.db = db_connector
        db_connector.get_duck_count.return_value = 0;
        app.decrease_duck_count()
        self.assertFalse(db_connector.decrease_duck_count.called)

if __name__ == '__main__':
    unittest.main()