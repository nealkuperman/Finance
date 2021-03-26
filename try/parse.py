import sys
import re
x = 5
print ("Hello")
def lesson_lines ():
    lesson_text = """
    *  History
          o Read Flags of the Tribes of Israel and enhance/modify your descriptions of tribal symbols. You may also want to look at Tribes and Sign's of the Zodiak Why is Asher represented by an Olive tree?
          o You say "Even after Moses, they still each believed in their own tribal gods." When did Moses live? How does that affect your answer? When did they begin to believe in Yahweh? When did they have tribal gods?
    * Holidays
          o Passover
                + both short and long descriptions much better at emphasizing our positive secular values - good start!
                + Short description - When were the Jews enslaved in Egypt? How can we remember mythical events? Better to add how the story inspires people to fight for freedom(Warsaw ghetto, abolitionists, possibly recent Russian Jewish exodus)
                + Long description - What we celebrate and how it influences and gives meaning to our lives is the most important part. The mythical story itself is of less importance and the fact that it is a myth should be in your description. Modify your description so that the amount of text is proportional to its importance to us (ie the part on morals, celebrating it every year and inspiring ancient and modern fights for freedom should be longer than the part on the mythical history - you may have to condense the myth part). You may also want to have a 3 or 4 line sentence about some highpoints of the seder - eg - reminders of what it might be like to be a slave, presence of an orange to be inclusive, importance given to children (4 questions, afikomen), encouraging discussion and analysis, favorite songs, etc
          o Purim
                + Modify long description to have positive secular values first. Was it necessary to kill the 70,000 or was the lack of taking booty a sign of a holy war like a Muslim Jihad and what are our feelings about that?
    * Culture
    * Heros
          o Spinoza
                + Nice job on the rewrite of the long description
                + Good changes for the short description - now add a sentence at the very start that begins with "Secular Jews value Spinoza because..."
    * 7th Grade Curriculum
          o Interview yourself and write what it means for you to be Jewish and why you are Jewish
    * FAQs -
          o "How can you be Jewish and not believe in God" - Loved your short answer and your long answer gets a B+. Well done!
          o Add the question to FAQ #3. Nice job on the enhancements!
"""
    lines = re.split(r'[\r\n]+', lesson_text)
    return lines

print lesson_lines()    