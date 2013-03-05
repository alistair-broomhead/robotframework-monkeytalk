robotframework-monkeytalk
=========================

direct integration with monkeytalk:

This test case is used to click two points on a screen

| *** Settings *** |
| Library        | MonkeyTalk | 192.168.35.155 | thinktime=${1} |

| *** Test Cases *** |
| To profile and back |
|    | [Tags] | incomplete |
|    | ${Profile}= | Evaluate | ['270', '270', '40', '60'] |
|    | ${Back}= | Evaluate | ['40', '60', '40', '60'] |
|    | Monkeytalk Command | View | \#2 | drag | ${Profile} |
|    | Monkeytalk Command | View | \#2 | drag | ${Back} |
