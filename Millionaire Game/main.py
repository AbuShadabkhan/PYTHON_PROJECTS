questions = [
  ["Which planet is known as the Red Planet?", "Saturn", "Mars", "Venus", "Jupiter", 2],
  ["Who wrote the national anthem of India?", "Sarojini Naidu", "Rabindranath Tagore", "Subhas Chandra Bose", "Bankim Chandra Chatterjee", 2],
  ["Which is the smallest bone in the human body?", "Tibia", "Ulna", "Femur", "Stapes", 4],
  ["Which gas do plants absorb from the atmosphere for photosynthesis?", "Carbon dioxide", "Nitrogen", "Hydrogen", "Oxygen", 1],
  ["Who was the first Prime Minister of India?", "Sardar Vallabhbhai Patel", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Mahatma Gandhi", 3],
  ["What is the capital city of Australia?", "Sydney", "Canberra", "Melbourne", "Perth", 2],
  ["In which continent is the Sahara Desert located?", "Asia", "South America", "Africa", "Europe", 3],
  ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo", 3],
  ["What is the chemical symbol for water?", "H2O", "CO2", "NaCl", "O2", 1],
  ["Which element has atomic number 1?", "Helium", "Hydrogen", "Oxygen", "Carbon", 2],
  ["Who discovered penicillin?", "Marie Curie", "Alexander Fleming", "Louis Pasteur", "Albert Einstein", 2],
  ["What is the largest ocean on Earth?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
  ["Which language has the most native speakers worldwide?", "English", "Mandarin Chinese", "Spanish", "Hindi", 2],
  ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", 2],
  ["Which country hosted the 2016 Summer Olympics?", "China", "Brazil", "UK", "Greece", 2],
  ["What currency is used in Japan?", "Yuan", "Yen", "Won", "Dollar", 2],
  ["In computing, what does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing Unit", 2],
  ["Which organ in the human body is responsible for pumping blood?", "Liver", "Brain", "Heart", "Kidney", 3],
  ["What is the powerhouse of the cell?", "Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus", 2],
  ["Who is known as the Father of Computers?", "Bill Gates", "Charles Babbage", "Steve Jobs", "Alan Turing", 2],
  ["What is the largest mammal in the world?", "African Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
  ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "Thailand", "South Korea", 2],
  ["What is the boiling point of water at sea level in Celsius?", "90°C", "95°C", "100°C", "110°C", 3],
  ["Who invented the telephone?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi", 1],
  ["Which planet has the most rings?", "Jupiter", "Neptune", "Saturn", "Uranus", 3],
  ["Who wrote 'The Odyssey'?", "Homer", "Virgil", "Dante", "Shakespeare", 1],
  ["What is the main language spoken in Brazil?", "Spanish", "Portuguese", "French", "English", 2],
  ["Which instrument measures atmospheric pressure?", "Thermometer", "Barometer", "Hygrometer", "Anemometer", 2],
  ["What is the tallest mountain in the world?", "K2", "Kangchenjunga", "Mount Everest", "Lhotse", 3],
  ["Who painted 'Starry Night'?", "Claude Monet", "Vincent van Gogh", "Pablo Picasso", "Salvador Dalí", 2],
  ["What is the chemical symbol for gold?", "Ag", "Au", "Fe", "Hg", 2],
  ["Which country gifted the Statue of Liberty to the USA?", "France", "UK", "Germany", "Spain", 1],
  ["What is the hardest natural substance on Earth?", "Diamond", "Gold", "Iron", "Quartz", 1],
  ["Who developed the theory of relativity?", "Isaac Newton", "Galileo Galilei", "Albert Einstein", "Niels Bohr", 3],
  ["What organelle is responsible for protein synthesis?", "Endoplasmic reticulum", "Golgi apparatus", "Ribosome", "Lysosome", 3],
  ["Which gas is most abundant in the Earth's atmosphere?", "Oxygen", "Nitrogen", "Carbon dioxide", "Argon", 2],
  ["Who is the author of '1984'?", "George Orwell", "Aldous Huxley", "F. Scott Fitzgerald", "Ernest Hemingway", 1],
  ["What is the largest internal organ in the human body?", "Liver", "Heart", "Lung", "Kidney", 1],
  ["Which element is used in light bulb filaments?", "Copper", "Iron", "Tungsten", "Aluminum", 3],
  ["What is the capital of Canada?", "Toronto", "Vancouver", "Ottawa", "Montreal", 3],
  ["Who painted the ceiling of the Sistine Chapel?", "Leonardo da Vinci", "Raphael", "Michelangelo", "Donatello", 3],
  ["What metal is liquid at room temperature?", "Mercury", "Lead", "Sodium", "Gold", 1],
  ["Which planet is closest to the Sun?", "Venus", "Mercury", "Earth", "Mars", 2],
  ["Who is the author of 'Pride and Prejudice'?", "Charlotte Brontë", "Jane Austen", "Mary Shelley", "Emily Brontë", 2],
  ["What is the process by which plants make their food?", "Digestion", "Photosynthesis", "Respiration", "Transpiration", 2],
  ["Which continent has the most countries?", "Africa", "Europe", "Asia", "South America", 1],
  ["What is the smallest prime number?", "0", "1", "2", "3", 3],
  ["Who discovered gravity after watching a falling apple?", "Galileo", "Isaac Newton", "Albert Einstein", "Johannes Kepler", 2],
  ["What is the chemical formula for table salt?", "NaCl", "KCl", "CaCl2", "MgCl2", 1],
  ["Which ocean lies between Africa and Australia?", "Pacific", "Atlantic", "Indian", "Arctic", 3]
]


prizes = [
    1000, 3000, 5000, 10000, 15000, 20000, 30000, 45000, 55000,
    65000, 75000, 85000, 100000, 125000, 150000, 200000, 300000,
    500000, 750000, 1000000, 1500000, 2000000, 3000000, 5000000,
    7500000, 10000000, 15000000, 20000000, 30000000, 50000000,
    75000000, 100000000, 150000000, 200000000, 300000000, 500000000,
    750000000, 1000000000, 1500000000, 2000000000, 3000000000, 5000000000,
    7500000000, 10000000000, 15000000000, 20000000000, 30000000000, 50000000000
]


i = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    # check whether the answer is correct or not
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5] == a):
        print("Correct answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break    
    print(f"You won {prizes[i]}")
    i += 1