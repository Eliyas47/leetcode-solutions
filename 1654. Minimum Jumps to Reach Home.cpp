class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        const int LIMIT = 6000;

        vector<bool> blocked(LIMIT + 1, false);
        vector<vector<bool>> visited(
            LIMIT + 1, vector<bool>(2, false)
        );

        for (int pos : forbidden) {
            blocked[pos] = true;
        }

        // {position, last jump was backward}
        queue<pair<int, bool>> q;
        q.push({0, false});
        visited[0][0] = true;

        int jumps = 0;

        while (!q.empty()) {
            int size = q.size();

            while (size--) {
                auto [pos, lastBack] = q.front();
                q.pop();

                if (pos == x) {
                    return jumps;
                }

                // Jump forward
                int forward = pos + a;

                if (forward <= LIMIT &&
                    !blocked[forward] &&
                    !visited[forward][0]) {

                    visited[forward][0] = true;
                    q.push({forward, false});
                }

                // Jump backward only if the previous jump
                // was not backward
                int backward = pos - b;

                if (!lastBack &&
                    backward >= 0 &&
                    !blocked[backward] &&
                    !visited[backward][1]) {

                    visited[backward][1] = true;
                    q.push({backward, true});
                }
            }

            jumps++;
        }

        return -1;
    }
};
