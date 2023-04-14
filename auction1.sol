pragma solidity ^0.8.0;

contract Auction {
    address public owner;
    uint public auctionEndTime;
    uint public highestBid;
    address public highestBidder;
    bool public ended;
    mapping(address => uint) public bids;

    event HighestBidIncreased(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);

    constructor(uint _biddingTime, uint _desiredPrice) {
        owner = msg.sender;
        auctionEndTime = block.timestamp + _biddingTime;
        highestBid = _desiredPrice;
        ended = false;
    }

    function bid() public payable {
        require(block.timestamp <= auctionEndTime, "Auction already ended.");
        require(msg.value > highestBid, "There already is a higher bid.");
        if (highestBidder != address(0)) {
            bids[highestBidder] += highestBid;
        }
        highestBidder = msg.sender;
        highestBid = msg.value;
        emit HighestBidIncreased(msg.sender, msg.value);
    }

    function finish() public {
        require(msg.sender == owner, "Only the owner can end the auction.");
        require(block.timestamp >= auctionEndTime, "Auction not yet ended.");
        require(!ended, "Auction has already been ended.");
        ended = true;
        emit AuctionEnded(highestBidder, highestBid);
        payable(owner).transfer(highestBid);
    }
}
