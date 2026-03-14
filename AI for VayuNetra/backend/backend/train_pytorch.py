import torch
import torch.nn as nn

X = torch.tensor([[120.0],[130.0],[140.0]])
y = torch.tensor([[130.0],[140.0],[150.0]])

class AQINet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1,1)

    def forward(self,x):
        return self.fc(x)

model = AQINet()

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(500):
    output = model(X)
    loss = criterion(output,y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

torch.save(model.state_dict(),"model/pytorch_model.pth")