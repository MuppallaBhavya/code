# sentence="my family consists of amma nanna akka anna"
def paindrome_case(sentence):
    sentence=sentence.split(" ")
    palindrome_exists=False
    for i in range(len(sentence)):
        if sentence[i][::-1]==sentence[i]:
            palindrome_exists=True
            print("palindrome")
            break
        if palindrome_exists ==False:
            print("not a palindrome")
paindrome_case("my family consists of amma nanna akka anna")
