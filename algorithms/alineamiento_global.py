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
            score = match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score
            diagonal = dp[i - 1][j - 1] + score
            left = dp[i][j - 1] + gap_penalty
            up = dp[i - 1][j] + gap_penalty
            dp[i][j] = max(diagonal, left, up)
    
    final_score = dp[len_seq1][len_seq2]
    return final_score


def backtrack(alignments, seq1, seq2, i, j, alignment_seq1, alignment_seq2, match_score, mismatch_score, gap_penalty):
    global dp
    if i == 0 and j == 0:
        alignments.append((alignment_seq1, alignment_seq2))
        return
    if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
        backtrack(alignments, seq1, seq2, i - 1, j - 1, seq1[i - 1] + alignment_seq1, seq2[j - 1] + alignment_seq2, match_score, mismatch_score, gap_penalty)
    if i > 0 and dp[i][j] == dp[i - 1][j] + gap_penalty:
        backtrack(alignments, seq1, seq2, i - 1, j, seq1[i - 1] + alignment_seq1, "-" + alignment_seq2, match_score, mismatch_score, gap_penalty)
    if j > 0 and dp[i][j] == dp[i][j - 1] + gap_penalty:
        backtrack(alignments, seq1, seq2, i, j - 1, "-" + alignment_seq1, seq2[j - 1] + alignment_seq2, match_score, mismatch_score, gap_penalty)


def needleman_wunsch_alignment(seq1, seq2, match_score, mismatch_score, gap_penalty):
    global dp
    needleman_wunsch_score(seq1, seq2, match_score, mismatch_score, gap_penalty)
    
    alignments = []
    alignment_seq1 = ""
    alignment_seq2 = ""

    backtrack(alignments, seq1, seq2, len(seq1), len(seq2), alignment_seq1, alignment_seq2, match_score, mismatch_score, gap_penalty)
    
    return alignments
