function [root, scenario] = currentScenario()

app = actxGetRunningServer('STK11.application');

% Grab a handle on the STK application root.
root = app.Personality2;

scenario = root.CurrentScenario;