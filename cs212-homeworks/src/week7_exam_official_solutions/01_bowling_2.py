## In the solution above, score_frame does most of the work, deciding the
## score for the frame, and what balls remain for subsequent frames.
## The logic of summing results is obscured by the need to return 2 values.
## An alternative solution below that makes it more explicit that we are summing 
## the 10 frames scores, by mutating balls rather than returning a 2nd value:

def bowling(balls):
    "Compute the score for one player's game of bowling."
    return sum(score_frame1(balls) for frame in range(10))

def score_frame1(balls):
    "Return (score, balls): the score for this frame and the remaining balls."
    n_used, n_scoring = ((1, 3) if balls[0] == 10 # strike
                    else (2, 3) if balls[0] + balls[1] == 10 # spare
                    else (2, 2)) # open frame
    score = sum(balls[:n_scoring])
    balls[:n_used] = []
    return score

def test_bowling():
    assert   0 == bowling([0] * 20)
    assert  20 == bowling([1] * 20)
    assert  80 == bowling([4] * 20)
    assert 190 == bowling([9,1] * 10 + [9])
    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5,5] * 5 + [10])
    assert  11 == bowling([0,0] * 9 + [10,1,0])
    assert  12 == bowling([0,0] * 8 + [10, 1,0])
