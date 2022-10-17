{
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "# 8.13 Exercises\n# Exercise 2\n# There is a string method called count that is similar to the function in Section 8.7.\n# Read the documentation of this method and write an invocation that counts the number\n# of a’s in 'banana'.\n\nword = 'banana'\ncount = 0\nindex_a = word.count('a')\nindex_a\n\n# I had little trouble using the count string method. I thought this exercise was easy.",
      "metadata": {
        "trusted": true
      },
      "execution_count": 3,
      "outputs": [
        {
          "execution_count": 3,
          "output_type": "execute_result",
          "data": {
            "text/plain": "3"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "# Exercise 3\n# A step size of -1 goes through the word backwards, so the slice [::-1] generates a\n# reversed string. Use this idiom to write a one-line version of is_palindrome\n# from Exercise 3.\n\ndef is_palindrome(word):\n    if word == word[::-1]:\n        return True\n    else:\n        return False\nis_palindrome('redivider')\n\n# It took a little while to fully understand what the slice [::-1] did, but now that I do,\n# I can see how useful it is for many contexts.",
      "metadata": {
        "trusted": true
      },
      "execution_count": 15,
      "outputs": [
        {
          "execution_count": 15,
          "output_type": "execute_result",
          "data": {
            "text/plain": "True"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    }
  ]
}
