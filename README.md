## Local development

### Run the server

1. Install python on your system
2. Move to the root directory of the project and create python virtual environment
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
4. Install the required python packages
    ```bash
    pip install -r requirements.txt
    ```
5. Run the code generation
    ```bash
    python main.py
    ```

### Program output for k=4 (15,11)
```
Message bits: [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
Codeword (15 bits): [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]
```

