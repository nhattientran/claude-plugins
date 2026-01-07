# gRPC Patterns

## Proto Definition
Follow [buf](https://buf.build/docs/best-practices/style-guide) style.

```proto
syntax = "proto3";

package v1;
option go_package = "github.com/org/repo/pkg/api/v1";

service UserService {
    rpc GetUser(GetUserRequest) returns (GetUserResponse);
}

message GetUserRequest {
    string id = 1;
}

message GetUserResponse {
    string id = 1;
    string email = 2;
}
```

## Service Implementation

```go
type UserServer struct {
    v1.UnimplementedUserServiceServer
    usecase usecase.UserUsecase
}

func (s *UserServer) GetUser(ctx context.Context, req *v1.GetUserRequest) (*v1.GetUserResponse, error) {
    user, err := s.usecase.GetByID(ctx, req.Id)
    if err != nil {
        return nil, status.Errorf(codes.NotFound, "user not found")
    }
    return &v1.GetUserResponse{Id: user.ID, Email: user.Email}, nil
}
```

## Interceptors
Use for logging, auth, and recovery.

```go
func LoggingInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
    log.Printf("gRPC method: %s", info.FullMethod)
    return handler(ctx, req)
}
```
