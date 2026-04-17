for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end = " ")
    print()

# WERSJA ŁADNIEJSZA, ZAPROPONOWANA PRZEZ CHATGPT
# print("   ", end="")
# for j in range(1, 6):
#     print(f"{j:4}", end="")
# print()

# for i in range(1, 6):
#     print(f"{i:3}", end="")
#     for j in range(1, 6):
#         print(f"{i * j:4}", end="")
#     print()