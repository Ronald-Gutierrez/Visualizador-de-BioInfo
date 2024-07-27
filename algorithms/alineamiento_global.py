def needleman_wunsch_score(seq1, seq2, match_score, mismatch_score, gap_penalty):
    global dp
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    dp = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]
    for i in range(1, len_seq1 + 1):
        dp[i][0] = i * gap_penalty
    for j in range(1, len_seq2 + 1):
        dp[0][j] = j * gap_penalty

    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            score = match_score if seq1[i -
                                        1] == seq2[j - 1] else mismatch_score
            diagonal = dp[i - 1][j - 1] + score
            left = dp[i][j - 1] + gap_penalty
            up = dp[i - 1][j] + gap_penalty
            dp[i][j] = max(diagonal, left, up)

    final_score = dp[len_seq1][len_seq2]
    return final_score


def globalTraceback(sequence1: str, sequence2: str, match_score, mismatch_score, gap_penalty):
    global dp
    alignments = []
    i = len(sequence1)
    j = len(sequence2)

    def backtrack(i, j, alignment_seq1, alignment_seq2):
        if i == 0 and j == 0:
            alignments.append((alignment_seq1, alignment_seq2))
            return
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (match_score if sequence1[i - 1] == sequence2[j - 1] else mismatch_score):
            backtrack(i - 1, j - 1,
                      sequence1[i - 1] + alignment_seq1, sequence2[j - 1] + alignment_seq2)
        if i > 0 and dp[i][j] == dp[i - 1][j] + gap_penalty:
            backtrack(i - 1, j,
                      sequence1[i - 1] + alignment_seq1, "-" + alignment_seq2)
        if j > 0 and dp[i][j] == dp[i][j - 1] + gap_penalty:
            backtrack(i, j - 1, "-" + alignment_seq1,
                      sequence2[j - 1] + alignment_seq2)
    backtrack(i, j, "", "")
    return alignments


# def needleman_wunsch_alignment(seq1, seq2, match_score, mismatch_score, gap_penalty):
#     global dp
#     needleman_wunsch_score(seq1, seq2, match_score,
#                            mismatch_score, gap_penalty)

#     alignments = []
#     alignment_seq1 = ""
#     alignment_seq2 = ""

#     backtrack(alignments, seq1, seq2, len(seq1), len(seq2), alignment_seq1,
#               alignment_seq2, match_score, mismatch_score, gap_penalty)

#     return alignments
