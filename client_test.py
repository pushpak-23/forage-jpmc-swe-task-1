import unittest
from client3 import getDataPoint


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            expected_result = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                               (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            self.assertEqual(getDataPoint(quote), expected_result, "Incorrect calculated values")

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            expected_result = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                               (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            self.assertEqual(getDataPoint(quote), expected_result, "Incorrect calculated values")

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_priceIsAverageOfBidAndAsk(self):
        quote = {'top_ask': {'price': 10.0, 'size': 10}, 'timestamp': '2021-06-28 12:00:00',
                 'top_bid': {'price': 9.0, 'size': 20}, 'id': '123', 'stock': 'XYZ'}
        stock, bid_price, ask_price, price = getDataPoint(quote)
        expected_price = (9.0 + 10.0) / 2
        self.assertEqual(price, expected_price, "Incorrect price calculation")


if __name__ == '__main__':
    unittest.main()
