def test_count_ballot(count_ballot):
    count_ballot("trump")
    count_ballot("biden")
    count_ballot("green")
    count_ballot("")
    count_ballot("trumpbiden")