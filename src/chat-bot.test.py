def test_Bible_chatbot():
    # Test 1
    prompt = "What is the meaning of life?"
    expected_response = "The meaning of life is a question that has puzzled philosophers for centuries."
    assert Bible_chatbot(prompt) == expected_response

    # Test 2
    prompt = "Who is Jesus Christ?"
    expected_response = "Jesus Christ is the son of God and the savior of the world."
    assert Bible_chatbot(prompt) == expected_response

    # Test 3
    prompt = "What is the difference between the Old and New Testaments?"
    expected_response = "The Old Testament is the story of God's relationship with the Jewish people, while the New Testament is the story of Jesus Christ and the early Christian church."
    assert Bible_chatbot(prompt) == expected_response

    # Test 4
    prompt = "What is the significance of the Ten Commandments?"
    expected_response = "The Ten Commandments are a set of moral and religious laws given by God to Moses on Mount Sinai. They are considered the foundation of Jewish and Christian ethics."
    assert Bible_chatbot(prompt) == expected_response