function [root, scenario] = openSTK(filename)

if nargin == 0
  filename = 'Untitled';
end

app = actxserver('STK11.application');

app.UserControl = 1;

% Grab a handle on the STK application root.
root = app.Personality2;

scenario = root.Children.New('eScenario',filename);

root.ExecuteCommand('BatchGraphics * On');