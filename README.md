# AsmodeusY - Blockchain-Powered Document Verification System

![AsmodeusY Logo](https://cdn-icons-png.flaticon.com/512/2906/2906274.png)

## Overview

AsmodeusY is a cutting-edge document verification system that leverages blockchain technology to ensure the authenticity and integrity of documents. Our platform provides a secure, transparent, and immutable way to verify and track documents throughout their lifecycle.

## Features

- 🔐 Secure document verification using blockchain technology
- 📄 Support for multiple document formats
- ⚡ Real-time verification status
- 🔍 Transparent audit trail
- 🌐 Web-based interface
- 🔒 End-to-end encryption

## Tech Stack

- Frontend: HTML, TailwindCSS, JavaScript
- Backend: Python Flask
- Blockchain: Ethereum
- Database: SQLite/PostgreSQL
- Authentication: Web3

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.8 or higher
- Node.js and npm
- Git
- MetaMask browser extension
- Web browser (Chrome/Firefox recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AsmodeusY.git
cd AsmodeusY
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
BLOCKCHAIN_NETWORK_URL=your_ethereum_network_url
```

5. Initialize the database:
```bash
python init_db.py
```

## Running the Application

1. Start the Flask server:
```bash
flask run
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Connect your MetaMask wallet when prompted

## Project Structure

```
AsmodeusY/
├── app.py              # Main Flask application
├── static/             # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/          # HTML templates
├── blockchain/         # Blockchain integration code
├── models/            # Database models
├── utils/             # Utility functions
└── tests/             # Test files
```

## Usage

1. Register/Login to your account
2. Upload the document you want to verify
3. The system will generate a unique hash and store it on the blockchain
4. Share the verification link with others
5. Recipients can verify the document's authenticity using the link

## Screenshots

### Homepage
![Homepage](Screenshot%202025-04-04%20195039.png)
*Our modern homepage showcasing the blockchain-powered document verification system with an interactive 3D blockchain visualization*

### Services Page
![Services](Screenshot%202025-04-04%20195056.png)
*Document verification interface with MetaMask integration and drag-and-drop file upload functionality*

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Team

- CH Puneeth Varma (99220041457)
- [Team Member 2]
- [Team Member 3]
- [Team Member 4]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Project Link: [https://github.com/yourusername/AsmodeusY](https://github.com/yourusername/AsmodeusY) 