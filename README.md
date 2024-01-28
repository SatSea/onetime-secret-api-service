# One-Time Secret Api Service

## Overview

This project implements a secure, one-time secret sharing service using FastAPI and Poetry for dependency management. It allows users to create a secret which can be retrieved only once using a unique secret key and a secret phrase.

## Features

- **Create Secret**: Users can submit a secret along with a secret phrase to receive a unique secret key.
- **Retrieve Secret**: By providing the correct secret key and secret phrase, the secret can be retrieved. Each secret is only retrievable once.

## Getting Started

### Prerequisites

- Python 3.12 (or python 3.7 if you very want to)
- Poetry

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/SatSea/onetime-secret-api-service
   ```
2. Navigate to the project directory:
   ```
   cd onetime-secret-api-service
   ```
3. Install dependencies using Poetry:
   ```
   poetry install
   ```

### Running the Application

1. Activate the Poetry environment:
   ```
   poetry shell
   ```
2. Start the FastAPI server:
   
   * In dev mode:

    ```
    poetry run dev
    ```

   * In prod mode:

    ```
    poetry run prod
    ```

The API will be available at `http://127.0.0.1:8000`.

## Endpoint

View them in /docs endpoint

## Security

This project is intended for educational purposes and may not be secure for production use. Secrets are stored in mongoDB and are only retrievable once. 
**Encryption methods have not been audited by professionals, and therefore, the project should not be considered cryptographically secure for sensitive data.**

## License

This project is licensed under the [MIT License](LICENSE).