{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "values = pd.read_csv(\"naloga1.csv\").squeeze()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def numbers(data):\n",
    "    only_numbers = []\n",
    "    for i in values:\n",
    "        number = re.findall(r'\\d', i)\n",
    "\n",
    "        if len(number) == 1:\n",
    "            only_numbers.append(str(number[0])+str(number[0]))\n",
    "        else:\n",
    "            first_nmb = number[0]\n",
    "            last_nmb = number[-1]\n",
    "            only_numbers.append(str(first_nmb) + str(last_nmb))\n",
    "    \n",
    "    only_numbers2 = []\n",
    "    for n in only_numbers:\n",
    "        only_numbers2.append(int(n))\n",
    "    \n",
    "    return sum(only_numbers2)\n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "56416"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers(values)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "PART 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def give_me_numbers(data):\n",
    "    word_to_number = {\n",
    "            'zero': '0',\n",
    "            'one': '1',\n",
    "            'two': '2',\n",
    "            'three': '3',\n",
    "            'four': '4',\n",
    "            'five': '5',\n",
    "            'six': '6',\n",
    "            'seven': '7',\n",
    "            'eight': '8',\n",
    "            'nine': '9',\n",
    "            'orez': '0',\n",
    "            'eno': '1',\n",
    "            'owt': '2',\n",
    "            'eerht': '3',\n",
    "            'ruof': '4',\n",
    "            'evif': '5',\n",
    "            'xis': '6',\n",
    "            'neves': '7',\n",
    "            'thgie': '8',\n",
    "            'enin': '9',\n",
    "        }\n",
    "\n",
    "\n",
    "    final_list = []\n",
    "    for i in values:\n",
    "        b = re.findall(r'\\d|zero|one|two|three|four|five|six|seven|eight|nine', i, re.IGNORECASE)\n",
    "        c = re.findall(r'\\d|orez|eno|owt|eerht|ruof|evif|xis|neves|enin|thgie', i[::-1], re.IGNORECASE)  \n",
    "        list = []\n",
    "        list2 = []\n",
    "        for char in b:\n",
    "            try:\n",
    "                int_value = int(char)\n",
    "                nmb = True\n",
    "            except (TypeError, ValueError):\n",
    "                nmb = False\n",
    "            if nmb:\n",
    "                number = int(char)\n",
    "                list.append(str(number))\n",
    "            else:\n",
    "                number = char\n",
    "                list.append(word_to_number[number])\n",
    "                first_nmb = list[0]\n",
    "\n",
    "       \n",
    "        for char in c: \n",
    "            try:\n",
    "                int_value = int(char)\n",
    "                nmb = True\n",
    "            except (TypeError, ValueError):\n",
    "                nmb = False\n",
    "            if nmb:\n",
    "                number = int(char)\n",
    "                list2.append(str(number))\n",
    "            else:\n",
    "                number = char\n",
    "                list2.append(word_to_number[number])\n",
    "                last_nmb = list2[0]\n",
    "                \n",
    "        final_list.append(int(list[0]+list2[0]))\n",
    "    return sum(final_list)\n",
    "\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55902"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "give_me_numbers(values) "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
