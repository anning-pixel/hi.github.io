import webbrowser

def hello_bakla():
    response = input("Do you miss me bakla? (yes/no) ")
    
    if response.lower() == "yes":
        print("Edi, I miss you too!Ingat ka palagi")
        # Open a cute GIF (example link)
        webbrowser.open("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXM5ZXRhNm5zb21pcDQzem8xZXpndmJiZ2Y4Mm9memE1YzN6dWlmcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PZqWOOE2QyeZi/giphy.gif")
        # Play the song (example link)
        webbrowser.open("https://www.youtube.com/watch?v=OqBuXQLR4Y8") # Link to "Best Friend" by Rex Orange County
    elif response.lower() == "no":
         print("Edi wag!! sino ka ba? look oh I'm sad na.")
         # Open a sad GIF (example link)
         webbrowser.open("https://media.giphy.com/media/fuDUlcnXPIGQ3AQaYj/giphy.gif?cid=ecf05e47xo0724s2vwrky5q7bfxz1swfak6wno8rhgu9g0qw&ep=v1_gifs_search&rid=giphy.gif&ct=g")
    else:
        print("ano di ka sasagot? 'yes or no' lang bakla.")

hello_bakla()