{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "# Variables to be used to store gathered information\n",
    "i = 0 \n",
    "j = 1\n",
    "total =[]\n",
    "ol = []\n",
    "cl = []\n",
    "\n",
    "#file path relative to the working directory\n",
    "budget_csv = os.path.join(\"budget_data.csv\")\n",
    "\n",
    "with open(budget_csv, newline = \"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = \",\")\n",
    "    # next allows to remove the next row (current row) and\n",
    "    csv_header = next(csvreader)\n",
    "    # Each row is a list\n",
    "    for row in csvreader:\n",
    "        #Store every month in a list\n",
    "        ol.append(row)\n",
    "       \n",
    "        \n",
    "# The total amount of months\n",
    "mnth_total = len(ol)\n",
    "\n",
    "# Prints the net sum\n",
    "for z in range(len(ol)):\n",
    "    total.append(int(ol[z][1]))\n",
    "period_sum = sum(total)\n",
    "\n",
    "# For loop to calculate and store monthly avaerages\n",
    "for i in range(len(ol)-1):\n",
    "    if j == range(len(ol)):\n",
    "        j = 86\n",
    "        cl.append(int(ol[j+1][1]) - int(ol[i+1][1]))\n",
    "        j += 1\n",
    "    else:\n",
    "        cl.append(int(ol[j][1]) - int(ol[i][1]))\n",
    "        j += 1\n",
    "\n",
    "\n",
    "# Computes average monthly change\n",
    "avg_mthly_chng = round(sum(cl)/len(cl),2)\n",
    "# Finds greatest increase in profit change\n",
    "max_incr_prof = max(cl)\n",
    "max_ind = cl.index(max(cl))\n",
    "max_mnth_incr = ol[max_ind + 1][0] + \" ($\" + str(max_incr_prof) + \")\"\n",
    "# Finds greatest decrease in profit change\n",
    "max_decr_prof = min(cl)\n",
    "min_ind = cl.index(min(cl))\n",
    "max_mnth_decr = ol[min_ind + 1][0] + \" ($\" + str(max_decr_prof) + \")\"\n",
    "\n",
    "with open (\"PyBank_Results.txt\", \"w\") as test_file:\n",
    "    print(f\"Financial Analysis\")\n",
    "    print(f\"----------------------------\")    \n",
    "    print(f\"Total Months: {mnth_total}\")\n",
    "    print(f\"Total: ${period_sum}\")\n",
    "    print(f\"Average Change: ${avg_mthly_chng}\")\n",
    "    print(f\"Greatest Increase in Profits: {max_mnth_incr}\")\n",
    "    print(f\"Greatest Decrease in Profits: {max_mnth_decr}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
