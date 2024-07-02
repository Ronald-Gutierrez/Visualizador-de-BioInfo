# def remove_spaces(s):
#     return s.replace(' ', '')

def smith_waterman(seq1, seq2, match_score, mismatch_score, gap_penalty):
    # formated_sequence1 = remove_spaces(seq1)
    # formated_sequence2 = remove_spaces(seq2)

    formated_sequence1 = seq1
    formated_sequence2 = seq2

    m = len(formated_sequence1)
    n = len(formated_sequence2)

    dp = [[(0, -1) for _ in range(n + 1)] for _ in range(m + 1)]

    max_score = 0
    max_score_pos = []

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dp[i - 1][j - 1][0] + (match_score if formated_sequence1[i - 1]
                                           == formated_sequence2[j - 1] else mismatch_score)
            delete_gap = dp[i - 1][j][0] + gap_penalty
            insert_gap = dp[i][j - 1][0] + gap_penalty

            max_current_score = max(0, match, delete_gap, insert_gap)

            traceback = -1
            if max_current_score == match:
                traceback = 0
            elif max_current_score == delete_gap:
                traceback = 1
            elif max_current_score == insert_gap:
                traceback = 2

            dp[i][j] = (max_current_score, traceback)

            if max_current_score > max_score:
                max_score = max_current_score
                max_score_pos = [(i, j)]
            elif max_current_score == max_score:
                max_score_pos.append((i, j))

    results = []
    for pos in max_score_pos:
        common_subsequence = ""
        i, j = pos

        while i > 0 and j > 0 and dp[i][j][0] > 0:
            if dp[i][j][1] == 0:
                common_subsequence = formated_sequence1[i -
                                                        1] + common_subsequence
                i -= 1
                j -= 1
            elif dp[i][j][1] == 1:
                i -= 1
            elif dp[i][j][1] == 2:
                j -= 1
            else:
                break

        results.append((max_score, max_score_pos, common_subsequence))

    return results
