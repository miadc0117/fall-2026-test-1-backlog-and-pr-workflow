```python
# boss_mini.py
# Security Audit: SECRET_CODE was a hardcoded credential and created a security backdoor.
# Fix: remove SECRET_CODE and the cheat logic.

p_hp = 50
b_hp = 50
MAX_HP = 50

# The Boss's health must be reduced when the player attacks.
# Fix: subtract 10 from b_hp when the player attacks.
def attack():
    global b_hp
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

# The player could heal above 50 HP or heal when their HP was 0 or less.
# Fix: check the player's HP before healing and keep it at 50 or below.
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

    # The cheat option was removed to close the security backdoor.
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    # The game needs to detect when the Boss reaches 0 HP.
    # Fix: print "Victory!" and stop the loop when b_hp <= 0.
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
```
