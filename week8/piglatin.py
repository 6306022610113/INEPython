def main():
    enter = input('Enter your sentense to change to pig latin : ')
    s = (enter.split())
    for i in range(s):
        x = (enter[0])
        if x == "A""E""I""O""U":
            print(enter[1:]+x+'HAY')
        else:
            print(enter[1:]+x+'AY')
    

main()