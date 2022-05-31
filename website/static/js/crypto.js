let keyPair, exportedKey;

async function generateKeys() {
    //Function for generating ECDH key pair
    keyPair = await crypto.subtle.generateKey(
        {
            name: "ECDH",
            namedCurve: "P-256"
        },
        true,
        ["deriveKey"]
    );
}

async function deriveKey(privateKey, publicKey) {
    //Function for deriving key for encryption
    return await window.crypto.subtle.deriveKey(
    {
        name: "ECDH",
        public: publicKey
    },
    privateKey,
    {
        name: "AES-GCM",
        length: 256
    },
    false,
    ["encrypt", "decrypt"]
    );
}

async function exportKey(keyPair) {
    //Function for exporting public key
    let temp = await window.crypto.subtle.exportKey("jwk", keyPair.publicKey)
    return temp
}

async function importKey(publicKey) {
    //Function for importing public key
    let temp = await window.crypto.subtle.importKey("jwk", publicKey, {name: "ECDH", namedCurve: "P-256"}, true, [])
    return temp
}

//Generate key pair
generateKeys()