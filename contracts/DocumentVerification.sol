// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVerification {
    struct Document {
        bytes32 hash;
        address owner;
        uint256 timestamp;
        bool isVerified;
    }
    
    mapping(bytes32 => Document) public documents;
    mapping(address => bytes32[]) public userDocuments;
    
    event DocumentVerified(bytes32 indexed hash, address indexed owner, uint256 timestamp);
    
    function verifyDocument(bytes32 _hash) public payable {
        require(!documents[_hash].isVerified, "Document already verified");
        
        documents[_hash] = Document({
            hash: _hash,
            owner: msg.sender,
            timestamp: block.timestamp,
            isVerified: true
        });
        
        userDocuments[msg.sender].push(_hash);
        
        emit DocumentVerified(_hash, msg.sender, block.timestamp);
    }
    
    function isDocumentVerified(bytes32 _hash) public view returns (bool, uint256, address) {
        Document memory doc = documents[_hash];
        return (doc.isVerified, doc.timestamp, doc.owner);
    }
    
    function getUserDocuments() public view returns (bytes32[] memory) {
        return userDocuments[msg.sender];
    }
} 