file = open('elfcalories.txt', 'r')
count = 1
subtot = 0
elf_tally = {}
for line in file:
    
    if len(line.strip()) == 0 :
        elf_tally[str(count)] = str(subtot)
        count += 1
        subtot = 0
        continue

    subtot += int(line.strip())

best_elf = 0
calories = 0
for elf in elf_tally:
    if int(elf_tally[elf]) > calories:
        best_elf = elf
        calories = int(elf_tally[elf])

top_elves = {}
top_elves[str(best_elf)] = calories
elf_tally[best_elf] = 0 

best_elf = 0
calories = 0
for elf in elf_tally:
    if int(elf_tally[elf]) > calories:
        best_elf = elf
        calories = int(elf_tally[elf])


top_elves[str(best_elf)] = calories
elf_tally[best_elf] = 0 
best_elf = 0
calories = 0
for elf in elf_tally:
    if int(elf_tally[elf]) > calories:
        best_elf = elf
        calories = int(elf_tally[elf])
top_elves[str(best_elf)] = calories
print(top_elves)
