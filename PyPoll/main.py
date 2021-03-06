{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 3521001\n",
      "-------------------------\n",
      "Khan: 63.000% (2218231)\n",
      "Correy: 20.000% (704200)\n",
      "Li: 14.000% (492940)\n",
      "O'Tooley: 3.000% (105630)\n",
      "-------------------------\n",
      "Winner: Khan\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "# Empty list to be used\n",
    "file_list = []\n",
    "khn = []\n",
    "cory = []\n",
    "li = []\n",
    "otly = []\n",
    "\n",
    "#file path relative to the working directory\n",
    "election_data_csv = os.path.join(\"election_data.csv\")\n",
    "\n",
    "with open(election_data_csv, newline = \"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = \",\")\n",
    "    # next allows to remove the next row (current row) and\n",
    "    csv_header = next(csvreader)\n",
    "    # Each row is a list\n",
    "    for record in csvreader:\n",
    "        #Store every month in a list\n",
    "        file_list.append(record)\n",
    "       \n",
    "        \n",
    "# The total amount of voters\n",
    "voter_total = len(file_list)\n",
    "\n",
    "# prints the net sum\n",
    "for z in range(len(file_list)):\n",
    "    if file_list[z][2] == \"Khan\":        \n",
    "        khn.append(file_list[z][2])\n",
    "    elif file_list[z][2] == \"Correy\": \n",
    "        cory.append(file_list[z][2])\n",
    "    elif file_list[z][2] == \"Li\":\n",
    "        li.append(file_list[z][2])\n",
    "    elif file_list[z][2] == \"O'Tooley\":\n",
    "        otly.append(file_list[z][2])\n",
    "\n",
    "# Khan's voter statistics\n",
    "khn_tot = len(khn)\n",
    "khn_per = khn_tot/voter_total*100\n",
    "# Correy's voter statistics\n",
    "cory_tot = len(cory)\n",
    "cory_per = (cory_tot/voter_total*100)\n",
    "# Li's voter statistics\n",
    "li_tot = len(li)\n",
    "li_per = (li_tot/voter_total*100)\n",
    "# O'Tooley's voter statistics\n",
    "otly_tot = len(otly)\n",
    "otly_per = otly_tot/voter_total*100\n",
    "\n",
    "# Dictionary of result totals\n",
    "poll_dict = {\"Khan\":khn_tot,\n",
    "       \"Correy\":cory_tot,\n",
    "            \"Li\":li_tot,\n",
    "            \"O'Tooley\":otly_tot}\n",
    "\n",
    "# Locates candidate with most votes to determine winner\n",
    "winner = max(poll_dict, key=poll_dict.get)\n",
    "\n",
    "with open (\"Poll_Results.txt\", \"w\") as text_file:\n",
    "    text_file.write(\"Election Results\\n\"\n",
    "    \"-------------------------\\n\"\n",
    "    f\"Total Votes: {voter_total}\\n\"\n",
    "    \"-------------------------\\n\"\n",
    "    f\"Khan: {'%.3f' % khn_per}% ({khn_tot})\\n\"\n",
    "    f\"Correy: {'%.3f' % cory_per}% ({cory_tot})\\n\"\n",
    "    f\"Li: {'%.3f' % li_per}% ({li_tot})\\n\"\n",
    "    f\"O'Tooley: {'%.3f' % otly_per}% ({otly_tot})\\n\"\n",
    "    \"-------------------------\\n\"\n",
    "    f\"Winner: {winner}\\n\"\n",
    "    \"-------------------------\\n\")\n",
    "    \n",
    "    print(\"Election Results\")\n",
    "    print(\"-------------------------\")\n",
    "    print(f\"Total Votes: {voter_total}\")\n",
    "    print(\"-------------------------\")\n",
    "    print(f\"Khan: {'%.3f' % khn_per}% ({khn_tot})\")\n",
    "    print(f\"Correy: {'%.3f' % cory_per}% ({cory_tot})\")\n",
    "    print(f\"Li: {'%.3f' % li_per}% ({li_tot})\")\n",
    "    print(f\"O'Tooley: {'%.3f' % otly_per}% ({otly_tot})\")\n",
    "    print(\"-------------------------\")\n",
    "    print(f\"Winner: {winner}\")\n",
    "    print(\"-------------------------\")"
   ]
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
